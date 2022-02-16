NAME 	=	pbrain-gomoku-ai

RM 		=	@rm -f
PRINT	=	@echo -e

SOURCES		=	src/

$(NAME):
	@cp $(SOURCES)main.py $@
	@chmod +x $@
	$(PRINT) "\n------->\tBINARY CREATED\n"

all: $(NAME)

exe:
	pyinstaller --onefile $(SOURCES)main.py
	@mv ./dist/main $(NAME).exe
	$(PRINT) "\n------->\tBINARY (.exe) CREATED\n"

clean:
	$(PRINT) "\n------->\tREMOVE PYCACHE\n"
	$(RM) -r __pycache__ $(SOURCES)__pycache__
	$(PRINT) "\n------->\tREMOVE BUILD TMP FILES\n"
	$(RM) -r *.pyc $(SOURCES)*.pyc

fclean: clean
	$(PRINT) "\n------->\tREMOVE BINARY\n"
	$(RM) $(NAME)
	$(RM) $(NAME).exe

re: fclean all

.PHONY: all clean fclean tests_run re