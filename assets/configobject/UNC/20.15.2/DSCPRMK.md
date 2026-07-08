---
id: UNC@20.15.2@ConfigObject@DSCPRMK
type: ConfigObject
name: DSCPRMK（重映射对应表）
nf: UNC
version: 20.15.2
object_name: DSCPRMK
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# DSCPRMK（重映射对应表）

## 说明

**适用网元：SGSN**

该命令用于对在PDP流控中“超出签约带宽”的报文设置处理规则。在PDP流控中，有部分数据报文“超出签约带宽”，对这部分报文可配置为“丢弃”，也可以进行DSCP(differentiated services code point)降级处理，使其对系统的影响减小。

该命令适用于Gn/Gp/Iu口的用户面数据报文。

DSCP降级处理共涉及到DSCP中的3大类，从高优先级到低优先级分别是：EF，AFx，BE；其中EF，BE的值都是固定的（二进制共6位；EF：101 110，BE:000 000），AFx根据二进制六位中的前3位，可以划分成0~7共8大类，但目前只使用1~4共4类，即AF1，AF2，AF3，AF4。

由EF转换为AFx时，只需把高3位转换为对应的值（例如：EF->AF2，即只把DSCP的高3位101直接修改为010，转换后的DSCP值为AF23），由EF(AFx)转换为BE时，直接修改成固定值（BE:000 000）即可;AFx之间进行转换时，只需要修改高3位的值（例如：DSCP:100110(AF43)转换为AF2时，把DSCP的高3位100直接修改为010，转换后的DSCP值为AF23）。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DSCPRMK]] · LST DSCPRMK
- [[command/UNC/20.15.2/SET-DSCPRMK]] · SET DSCPRMK

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSCPRMK.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPRMK.md`
