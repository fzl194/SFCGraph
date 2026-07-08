---
id: UNC@20.15.2@MMLCommand@LST ADDRN2TACID
type: MMLCommand
name: LST ADDRN2TACID（查询N2TAC组内N2TAC号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRN2TACID
command_category: 查询类
applicable_nf:
- GGSN
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配N2TAC段
status: active
---

# LST ADDRN2TACID（查询N2TAC组内N2TAC号段）

## 功能

**适用NF：GGSN、SMF、PGW-C**

该命令用来查询指定N2TAC号段与N2TAC组的绑定关系或者配置的所有N2TAC号段和N2TAC组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | N2TAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRTACGROUP命令配置生成。 |
| TACSECNUM | N2TAC段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRN2TACID]] · N2TAC组内N2TAC号段（ADDRN2TACID）

## 使用实例

查询指定N2TAC号段与N2TAC组的绑定关系：“N2TAC组”为“wz-sq”，“N2TAC号段”为“2”：

```
LST ADDRN2TACID:TACGROUPNAME="wz-sq",TACSECNUM=2;
RETCODE = 0  操作成功。

结果如下
------------------------
   N2TAC组名  =  wz-sq
 N2TAC段编号  =  2
 N2TAC起始ID  =  0x1
 N2TAC终止ID  =  0x1F
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ADDRN2TACID.md`
