package com.company;

import java.util.Scanner;
//import java.util.io;
import java.util.*;

public class CoWin {
	static Scanner scn = new Scanner(System.in);
	//hospitalID
	//i have used arraylists to store the hospitals, citizens, vaccine,slot as an arraylist is a 
	//dynamic data structure and we can use the add function to simply add records of the respective
	//entities dynamically whenever we want to.
	static ArrayList <hospital> hospitals = new ArrayList<hospital>();
	static ArrayList <citizen> citizens = new ArrayList<citizen>();
	static ArrayList <vaccine> vaccinesAvailable = new ArrayList<vaccine>();
	static ArrayList <slot> slots = new ArrayList<slot>();
	static int IDcounter = 100000;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("CoWin Portal initialized....");
		System.out.println("---------------------------------");
		//System.out.println("=================================");
		System.out.println("What do you want to do?");
		System.out.println("1. Add Vaccine\n"
				+ "2. Register Hospital\n"
				+ "3. Register Citizen\n"
				+ "4. Add Slot for Vaccination\n"
				+ "5. Book Slot for Vaccination\n"
				+ "6. List all slots for a hospital\n"
				+ "7. Check Vaccination Status\n"
				+ "8. Exit"
				);
		System.out.println("---------------------------------");
		int flag;
		flag = scn.nextInt();
		do {
			
			
			if(flag == 1) {
				addVaccine();
			}
			else if(flag == 2) {
				regHospital();
				IDcounter++;
			}
			
			else if(flag == 3) {
				regCitizen();
			}
			else if(flag == 4) {
				createSlots();
			}
			else if(flag == 5) {
				bookSlots();
			}
			else if(flag == 6) {
				slotsAvailable();
			}
			else if(flag == 7) {
				vaccinationStatus();
			}
			else if(flag == 8) {
				break;//
			}
			System.out.println();
			System.out.println();
			System.out.println("What do you want to do?");
			System.out.println("1. Add Vaccine\n"
					+ "2. Register Hospital\n"
					+ "3. Register Citizen\n"
					+ "4. Add Slot for Vaccination\n"
					+ "5. Book Slot for Vaccination\n"
					+ "6. List all slots for a hospital\n"
					+ "7. Check Vaccination Status\n"
					+ "8. Exit"
					);
			System.out.println("---------------------------------");
			System.out.println();
			flag = scn.nextInt();
		}while(flag!=8);
	}
	public static void addVaccine(){
		//Name, Number of total doses required, Gap Between Doses
		System.out.print("Vaccine name : ");
		String name = scn.next();
		//System.out.println();
		System.out.print("Number of Doses: ");
		int no_doses = scn.nextInt();
		//System.out.println();
		int gap = 0;
		if(no_doses !=1) {
			System.out.print("Gap between Doses: ");
			gap = scn.nextInt();
		}
		vaccine variant = new vaccine(name,no_doses,gap);
		vaccinesAvailable.add(variant);
		System.out.println("Vaccine Name: " + name + ", Number of Doses: " + no_doses + ", Gap Between Doses: " + gap);
		//addVaccine(name,no_doses,gap);
		return;
		
	}
	public static void regHospital() {
		System.out.print("Hospital name : ");
		String name = scn.next();
		//System.out.println();
		System.out.print("PinCode : ");
		
		int pin = scn.nextInt();
		
		
		hospital newHospital = new hospital(name,pin,IDcounter);
		hospitals.add(newHospital);
		System.out.println("Hospital Name: " + name + ", PinCode: " + pin + " Unique ID: " + newHospital.getHospitalID());
		return;
		
	}
	public static void regCitizen() {
		System.out.print("Citizen name : ");
		String name = scn.next();
		//System.out.println();
		System.out.print("Age: ");
		int age = scn.nextInt();
//		if(age<18) {
//			System.out.println("You should be above or equal to 18 to register to the portal !!");
//			return;
//		}
		//System.out.println();
		System.out.print("Unique ID: ");
		long uniqueID = scn.nextLong();
		boolean ID_exists = false;
		for(citizen citizen:citizens) {
			if(citizen.getCID() == uniqueID) {
				ID_exists = true;
			}
		}
		if(ID_exists) {
			System.out.println("Two users with the same ID can't exist");
		}
		else {
			citizen newCitizen = new citizen(name,age,uniqueID);
		
			if(age>=18) {
				citizens.add(newCitizen);
				System.out.println("Citizen Name: " + name + ", Age: " + age + ", Unique ID: " + uniqueID);
			}
			
			if(age<18) {
				System.out.println("Only above 18 are allowed");
				return;
			}
		}
		return;
		
		
//		Citizen Name: Marrion
//		Age: 23
//		Unique ID: 123456789000
//		Citizen Name: Marrion, Age: 23, Unique ID: 123456789000
	}
	public static void createSlots() {
		System.out.print("Enter Hospital ID : ");
		int ID = scn.nextInt();
		//handle the case in which the hospital ID is wrong
		//System.out.println();
		boolean h_found = false;
		for(hospital hospital:hospitals) {
			if(hospital.getHospitalID() == ID) {
				h_found = true;
			}
		}
		if(h_found) {
			System.out.print("Enter number of slots to be added: ");
			int no_slots = scn.nextInt();
			//System.out.println();
			for(int i = 0 ; i<no_slots ; i++) {
				System.out.print("Enter Day Number: ");
				int day_no = scn.nextInt();
				System.out.print("Enter Quantity: ");
				int quantity = scn.nextInt();
				System.out.println("Select vaccine-");
				int counter = 0;
				int vaccine_no;
				for(vaccine vacc:vaccinesAvailable) {
					System.out.println(counter + ". " + vacc.get_v_name());//
					counter++;
				}
				vaccine_no = scn.nextInt();
				String vacc_name = vaccinesAvailable.get(vaccine_no).get_v_name();//
				
				slot newSlot = new slot(ID,day_no,no_slots,quantity,vacc_name);
				slots.add(newSlot);
				System.out.println("Slot added by Hospital " + ID + " for Day: " + day_no + ", Available Quantity: " + quantity + " of Vaccine " + vacc_name);
			}
		}
		else {
			System.out.println("No hospital with the ID entered !!!");
		}
		return;
		
		//make a slot array list of type slots and keep adding the slots into it
//		Enter Hospital ID: 123456
//		Enter number of Slots to be added: 2
//		Enter Day Number: 1
//		Enter Quantity: 5
//		Select Vaccine
//		0. Covax
//		1. Covi
//		0
//		Slot added by Hospital 123456 for Day: 1, Available Quantity: 5 of Vaccine Covax
//		Enter Day Number: 2
//		Enter Quantity: 5
//		Select Vaccine
//		0. Covax
//		1. Covi
//		1
//		Slot added by Hospital 123456 for Day: 2, Available Quantity: 5 of Vaccine Covi
	}
	public static void bookSlots() {
		System.out.print("Enter patient unique ID : ");
		long ID = scn.nextLong();
		boolean IDfound = false;
		for(citizen citizen:citizens) {
			if(citizen.getCID() == ID) {
				IDfound = true;
				//citizen temp_citizen = citizen;
				break;
			}
		}
		
		//handle the case in which the hospital ID is wrong
		//System.out.println();
		if(IDfound) {
			System.out.println("1. Search by area");
			System.out.println("2. Search by Vaccine");
			System.out.println("3. Exit");
			System.out.print("Enter option: ");
			//System.out.println();
			int flag = scn.nextInt();
			int pincode;
			int counter = 0;
			boolean h_found = false ;
			if(flag == 1) {
				System.out.print("Enter pin code: ");
				pincode = scn.nextInt();
				
				for(hospital hospital:hospitals) {
					if(hospital.getPin() == pincode) {
						System.out.println(hospital.getHospitalID() + " " + hospital.getName());
						h_found = true;
					}
				}
				//removal of slots
				//
				//System.out.println();
				if(h_found) {
					System.out.print("Enter hospital id: ");
					int h_ID = scn.nextInt();
					ArrayList <slot> temp_slots = new ArrayList<slot>();
					boolean flag1 = true;
					
					for(slot slot:slots) {
						
						if(slot.getHospitalID() == h_ID) {
							flag1 = true;
							//temp_slots.add(slot);
							
							for(citizen citizen:citizens) {
								if(citizen.getCID() == ID) {
									String status = citizen.getStatus();
									
									if(status.equals("PARTIALLY VACCINATED")) {
										if(citizen.getDueDate()>slot.getSlotday()) {
											flag1 = false;
										}
										if(!citizen.getVaccname().equals(slot.getVaccineName())) {
											flag1 = false;
										}
									}
				
									else if(status.equals("FULLY VACCINATED")){
										flag1 = false;
									}
								}
							}
							if(flag1 == true) {
								//0-> Day: 1 Available Qty:5 Vaccine:Covax
								//System.out.println();
								if(slot.getNoDoses()>0) {
									System.out.println(counter + "-> Day: " + slot.getSlotday() + " Available Qty:" + slot.getNoDoses() + " Vaccine:" + slot.getVaccineName());
									counter++;
									temp_slots.add(slot);
								}
							
							}
						}
					}
					if(temp_slots.size() ==0) {
						System.out.println("No slots available");
					}
					//Choose Slot: 0
		//			Marrion vaccinated with Covax
					else {
						System.out.println();
						System.out.print("Choose Slot: ");
						int option;
						option = scn.nextInt();
						slot temp_slot = temp_slots.get(option);
						temp_slots.get(option).setNoDoses(temp_slot.getNoDoses()-1);
						vaccine vaccinated_with = null;
						for(citizen c:citizens) {
							if(c.getCID() == ID) {
								String cName = c.getC_name();
								System.out.println(cName + " vaccinated with " + temp_slot.getVaccineName());
								for(vaccine v:vaccinesAvailable) {
									if(v.get_v_name().equals(temp_slot.getVaccineName())) {
										c.setDueDate(temp_slot.getSlotday() + v.getGap());
										c.vaccinating(v);
										vaccinated_with = v;
									}
								}
								if(c.getStatus().equals("REGISTERED") && vaccinated_with.num_doses() != 1) {
									c.setStatus("PARTIALLY VACCINATED");
								}
								else if(vaccinated_with.num_doses() == 1 && c.getStatus().equals("REGISTERED")) {
									c.setStatus("FULLY VACCINATED");
								}
								else if(c.getStatus().equals("PARTIALLY VACCINATED")) {
									c.setStatus("FULLY VACCINATED");
								}
								if(temp_slots.get(option).getNoDoses() == 0) {
									;
								}
								
							}
							
						}
					}
				}
				else {
					System.out.println("No slots available");
				}
			}
			else if (flag == 2) {
	//			Enter patient Unique ID: 123456789000
	//			1. Search by area
	//			2. Search by Vaccine
	//			3. Exit
	//			Enter option: 2
	//			Enter Vaccine name: Covax
	//			123456 Medistar
	//			111111 HealthCenter
	//			Enter hospital id: 111111
	//			2-> Day: 3 Available Qty:10 Vaccine:Covax
	//			Choose Slot: 2
	//			Marrion vaccinated with Covax
				System.out.print("Enter Vaccine name: ");
				String vacc_req = scn.next();
				String prev_hospital = "temp";
				for(vaccine vaccine:vaccinesAvailable) {
					if(vaccine.get_v_name().equals(vacc_req)) {
						for(slot slot:slots) {
							if(slot.getVaccineName().equals(vacc_req)) {
								for(hospital hospital:hospitals) {
									if(slot.getHospitalID() == hospital.getHospitalID()) {
										if(!prev_hospital.equals(hospital.getName())) {
											System.out.println(slot.getHospitalID() + " " + hospital.getName());
											prev_hospital = hospital.getName();
										}
										h_found = true;
									}	
								}
							}	
						}
					}
				}
				if(h_found) {
					System.out.println();
					System.out.print("Enter hospital id: ");
					int h_ID = scn.nextInt();
					ArrayList <slot> temp_slots = new ArrayList<slot>();
					boolean flag1 = true;
					
					for(slot slot:slots) {
						if(slot.getHospitalID() == h_ID) {
							flag1 = true;
							//temp_slots.add(slot);
							
							for(citizen citizen:citizens) {
								if(citizen.getCID() == ID) {
									String status = citizen.getStatus();
									if(status.equals("PARTIALLY VACCINATED")) {
										if(citizen.getDueDate()>slot.getSlotday()) {
											flag1 = false;
										}
										if(!citizen.getVaccname().equals(slot.getVaccineName())) {
											flag1 = false;
										}
									}
									else if(status.equals("FULLY VACCINATED")){
										flag1 = false;
									}
								}
							}
							if(flag1 == true) {
								//0-> Day: 1 Available Qty:5 Vaccine:Covax
								//System.out.println();
								
								if(slot.getNoDoses()>0 && slot.getVaccineName().equals(vacc_req)) {
									System.out.println(counter + "-> Day: " + slot.getSlotday() + " Available Qty:" + slot.getNoDoses() + " Vaccine:" + slot.getVaccineName());
									counter++;
									temp_slots.add(slot);
								}
							}
						}
					}
					if(temp_slots.size() == 0) {
						System.out.println("No slots available");
					}
					//Choose Slot: 0
		//			Marrion vaccinated with Covax
					else {
						System.out.println();
						System.out.print("Choose Slot: ");
						int option;
						option = scn.nextInt();
						slot temp_slot = temp_slots.get(option);
						temp_slots.get(option).setNoDoses(temp_slot.getNoDoses()-1);
						vaccine vaccinated_with = null;
						for(citizen c:citizens) {
							if(c.getCID() == ID) {
								String cName = c.getC_name();
								System.out.println(cName + " vaccinated with " + temp_slot.getVaccineName());
								for(vaccine v:vaccinesAvailable) {
									if(v.get_v_name().equals(temp_slot.getVaccineName())) {
										c.setDueDate(temp_slot.getSlotday() + v.getGap());
										c.vaccinating(v);
										vaccinated_with = v;
									}
								}
								if(c.getStatus().equals("REGISTERED") && vaccinated_with.num_doses() != 1 ) {
									c.setStatus("PARTIALLY VACCINATED");
								}
								else if(vaccinated_with.num_doses() == 1 && c.getStatus().equals("REGISTERED")) {
									c.setStatus("FULLY VACCINATED");
								}
								else if(c.getStatus().equals("PARTIALLY VACCINATED")) {
									c.setStatus("FULLY VACCINATED");
								}
								if(temp_slots.get(option).getNoDoses() == 0) {
									;
								}
							}
							
						}
					}
				}
				else {
					System.out.println("No slots Available");
				}
			
			}
			else if(flag == 3) {
				return;
			}
		}
		else {
			System.out.println("Citizen with the entered ID does not exist");
			return;
		}
			
	}
	public static void slotsAvailable(){
//		Enter Hospital Id: 123456
//		Day: 1 Vaccine: Covax Available Qty: 5
//		Day: 2 Vaccine: Covi Available Qty: 5
		System.out.print("Enter Hospital Id: ");
		int h_ID = scn.nextInt();
		for(slot slot:slots) {
			if(slot.getHospitalID() == h_ID) {
				System.out.println("Day: " + slot.getSlotday() + " Vaccine: " + slot.getVaccineName() + " Available Qty: " + slot.getNoDoses());
			}
		}
	}
	public static void vaccinationStatus() {
//		Enter Patient ID: 123456789000
//		PARTIALLY VACCINATED
//		Vaccine Given: Covax
//		Number of Doses given: 1
//		Next Dose due date: 3

//		Enter Patient ID: 123456789000
//		FULLY VACCINATED
//		Vaccine Given: Covax
//		Number of Doses given: 2
//in test 2 gap is not added	
//		Enter Patient ID: 454545656565
//		Citizen REGISTERED
		System.out.print("Enter Patient ID: ");
		long patientID = scn.nextLong();
		for(citizen citizen:citizens) {
			if(citizen.getCID() == patientID) {
				if(citizen.getStatus().equals("PARTIALLY VACCINATED")) {
					System.out.println("PARTIALLY VACCINATED");
					System.out.println("Vaccine Given: " + citizen.getVaccname());
					System.out.println("Number of Doses given: " + citizen.getDoses());
					System.out.println("Next Dose due date: " + citizen.getDueDate());
				}
				else if(citizen.getStatus().equals("FULLY VACCINATED")) {
					System.out.println("FULLY VACCINATED");
					System.out.println("Vaccine Given: " + citizen.getVaccname());
					System.out.println("Number of Doses given: " + citizen.getDoses());
					//System.out.println("Next Dose due date: " + citizen.getDueDate());
				}
				else if(citizen.getStatus().equals("REGISTERED")) {
					System.out.println("REGISTERED");
				}
			}
		}
	}
}
//keep in mind to update the vaccination status
class slot{
	private int hospitalID;
	private int slot_day;
	private String vaccine_name;
	private int no_slots;
	private int no_doses;
	slot(int id , int slot_day,int no_slots,int no_doses, String vaccine_name){
		this.hospitalID = id;
		this.slot_day = slot_day;
		this.vaccine_name = vaccine_name;
		this.no_doses = no_doses;
		this.no_slots = no_slots;
	}
	public int getSlotday(){
		return slot_day;
	}
	public int getHospitalID(){
		return hospitalID;
	}
	public String getVaccineName() {
		return vaccine_name;
	}
	public int getNoDoses() {
		return no_doses;
	}
	public void setNoDoses(int new_no) {
		this.no_doses = new_no;
	}
	public int getNoSlots() {
		return no_slots;
	}
}
class citizen{
	private String c_name;
	private int age;
	private long uniqueID;
	private int next_dueDate = 0;
	private vaccine v = null;
	private int doses;
	private String status;
	//String vaccinationStatus;
	citizen(String name, int age , long uniqueID){
		this.c_name = name;
		this.age = age;
		this.uniqueID = uniqueID;
		this.status = "REGISTERED";
	}
	public String getC_name() {
		return c_name;
	}
	public long getCID() {
		return uniqueID;
	}
	public void setDueDate(int date) {
		this.next_dueDate = date;
	}
	public int getDueDate() {
		return next_dueDate;
	}
	public void setStatus(String status) {
		this.status = status;
	}
	public String getStatus() {
		return this.status;
	}
	//vaccinating call
	//
	public void vaccinating(vaccine v) {
		this.v = v;
		//this.next_dueDate = day + v.getGap();//
		this.setDoses(1);
	}
	public String getVaccname() {
		return this.v.get_v_name();
	}
	public void setDoses(int number){
		this.doses +=number;
	}
	public int getDoses(){
		return this.doses;
	}
	public int getAge(){
		return this.age;
	}
	
//	Enter patient Unique ID: 123456789000
//	1. Search by area
//	2. Search by Vaccine
//	3. Exit
//	Enter option: 1
//	Enter PinCode: 110091
//	123456 Medistar
//	Enter hospital id: 123456
//	0-> Day: 1 Available Qty:5 Vaccine:Covax
//	1-> Day: 2 Available Qty:5 Vaccine:Covi
//	Choose Slot: 0
//	Marrion vaccinated with Covax
}
class hospital{
	private String h_name;
	private int pincode;
	private int hospitalID;
	hospital(String name , int pincode,int ID){
		this.h_name = name;
		this.pincode = pincode;
		this.hospitalID = ID;
	}
	public int getPin() {
        return pincode;
    }

    public int getHospitalID() {
        return hospitalID;
    }
    public String getName() {
    	return h_name;
    }
}
class vaccine{
	private String v_name;
	private int num_doses;
	private int gap;
	vaccine(String name,int doses , int gap){
		this.v_name = name;
		this.num_doses = doses;
		this.gap = gap;
	}
	public String get_v_name() {
		return v_name;
	}
	public int getGap() {
		return gap;
	}
	public int num_doses() {
		return num_doses;
	}
	
}
