EXE =  ../bin/BSK_calc.x
OBJS = ap_tools.o  ap_mu_tools.o ap_cosmo_funs.o ap_settings_init.o ap_cell.o ap_smooth.o ap_grad_fields.o  ap_chisq.o ap_BSK.o
F90C = gfortran
F90FLAGS = 

all : $(EXE)
$(EXE): $(OBJS) ap_main_BSK_calc.o
	$(F90C) -o $(EXE) $(OBJS) ap_main_BSK_calc.o

ap_cosmo_funs.o: ap_tools.o
ap_mu_tools.o: ap_tools.o
ap_settings_init.o: ap_cosmo_funs.o 
ap_cell.o: ap_settings_init.o
ap_smooth.o: ap_cell.o
ap_grad_fields.o: ap_smooth.o ap_mu_tools.o
ap_chisq.o: ap_grad_fields.o 
ap_main_calc_grad_chisqs.o:  ap_chisq.o 
ap_BSK.o : ap_chisq.o
ap_main_BSK_calc.o: ap_BSK.o 
ap_main_test.o: ap_settings_init.o
ap_main_BSK_Scan.o: ap_BSK.o

%.o: %.f90
	$(F90C) -c $*.f90 $(F90FLAGS)

clean :
	rm -rf *.o *.mod $(EXE)
