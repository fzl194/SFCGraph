---
id: UNC@20.15.2@MMLCommand@DSP PTPBVC
type: MMLCommand
name: DSP PTPBVC（显示小区上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PTPBVC
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 小区管理
status: active
---

# DSP PTPBVC（显示小区上下文信息）

## 功能

**适用网元：SGSN**

该命令用于查询PTPBVC上下文信息。PTPBVC实体和小区标识在系统内互相唯一对应，通过 [**LST CELL**](查询小区(LST CELL)_26145990.md) 可以获得小区标识，再根据小区标识采用此命令可以查询对应的PTPBVC上下文相关信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | 小区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定小区的标识，CELLID = MCC + MNC + LAC + RAC + CI。<br>取值范围：长度不超过23的十六进制数<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PTPBVC]] · 复位小区（PTPBVC）

## 使用实例

查询小区标识为123031003031015的PTPBVC上下文信息：

DSP PTPBVC: CELLID="123031003031015";

```
%%DSP PTPBVC: CELLID="123031003031015";%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
                                          上下文是否分配  =  是
                                             PTP实体状态  =  正常状态
                                      是否接收到流控消息  =  是
                                          PTP实体所在NSE  =  11002
                                                 BVC标志  =  1015
                                         SIG实体所处位置  =  385876984
                                    PTP实体RESET重发次数  =  0
                                  BVC流控桶大小(100byte)  =  1024
                                   BVC泄漏速率(100bit/s)  =  1024
                             BVC流控桶内容量计数器(byte)  =  0
                             BVC上一个流控包通过的时刻Tp  =  0
                        BVC内MS缺省的流控桶大小(100byte)  =  195
                         BVC内MS缺省的泄漏速率(100bit/s)  =  260
                           PCU侧平均每包的传输延时(10ms)  =  65535
                                 该BVC下第一个MS控制表号  =  4294967295
                               该BVC下最后一个MS控制表号  =  4294967295
                                                下传标志  =  不传
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PTPBVC.md`
