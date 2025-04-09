‘  void remdiv(long x, long y, long *qp, long *rp)
  x in %rdi, y in %rsi, qp in %rdx, rp in %rcx
1	remdiv:
2	 movq %rdx, %r8		Copy qp
3	 movq %rdi, %rax	Move x to lower 8 bytes of dividend
4	 cqto			Sign-extend to upper 8 bytes of dividend
5	 idivq %rsi		Divide by y
6	 movq %rax, (%r8)	Store quotient at qp
7	 movq %rdx, (%rcx)	Store remainder at rp
8	 ret