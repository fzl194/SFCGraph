---
id: UNC@20.15.2@MMLCommand@LST LLCXID
type: MMLCommand
name: LST LLCXID（查询LLC协商参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LLCXID
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
- LLC参数
status: active
---

# LST LLCXID（查询LLC协商参数）

## 功能

**适用网元：SGSN**

该命令用于查询GBP进程LLC层XID协商参数配置。

## 注意事项

- 可以通过这个命令来查询之前通过[**ADD LLCXID**](增加LLC协商参数(ADD LLCXID)_72345615.md)配置的XID参数N201U，T200。没有配置的LLC参数将采用3GPP 44.064中的缺省值。
- 输入参数“SAPI”，查询指定SAPI的单条记录；不输入参数，查询已配置的所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SAPI | SAPI | 可选必选说明：可选参数<br>参数含义：该参数用于指定SAPI。<br>取值范围：<br>- “SAPI3(SAPI3)”<br>- “SAPI5(SAPI5)”<br>- “SAPI9(SAPI9)”<br>- “SAPI11(SAPI11)”<br>默认值：无<br>说明：SAPI3，SAPI5，SAPI9，SAPI11表示用户数据。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LLCXID]] · LLC协商参数（LLCXID）

## 使用实例

查询SAPI3的配置：

LST LLCXID: SAPI=SAPI3;

```
%%LST LLCXID: SAPI=SAPI3;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------------------------
                         SAPI  =  SAPI3
   SN-UNITDATA PDU 最大字节数  =  1520
             LLC重传定时器(s)  =  40
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LLCXID.md`
