---
id: UDG@20.15.2@MMLCommand@LST N2TACID
type: MMLCommand
name: LST N2TACID（查看N2TAC与N2TAC组的绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: N2TACID
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- N2TAC段
status: active
---

# LST N2TACID（查看N2TAC与N2TAC组的绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看指定N2TAC号段与N2TAC组的绑定关系或者配置的所有N2TAC号段和N2TAC组的绑定关系。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | 指定N2TAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定N2TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACSECNUM | N2Tac 段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/N2TACID]] · 从N2TAC组内删除一个TAC（N2TACID）

## 使用实例

假设运营商需要查看指定N2TAC号段与N2TAC组的绑定关系：N2TAC组为beijing，N2TAC号段为2：

```
LST N2TACID:TACGROUPNAME="beijing",TACSECNUM=2;
```

```

RETCODE = 0  操作成功。

结果如下
--------
  N2TAC段编号  =  2
  N2TAC起始ID  =  0x000001
  N2TAC截止ID  =  0x000010
指定TAC组名  =  beijing
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查看N2TAC与N2TAC组的绑定关系（LST-N2TACID）_97358683.md`
