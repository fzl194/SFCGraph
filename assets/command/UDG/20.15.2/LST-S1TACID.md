---
id: UDG@20.15.2@MMLCommand@LST S1TACID
type: MMLCommand
name: LST S1TACID（查看S1TAC与S1TAC组的绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: S1TACID
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- S1TAC段
status: active
---

# LST S1TACID（查看S1TAC与S1TAC组的绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看指定S1TAC号段与S1TAC组的绑定关系或者配置的所有S1TAC号段和S1TAC组的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | 指定S1TAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TACSECNUM | S1Tac 段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1TAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～15999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [从S1TAC组内删除一个S1TAC（S1TACID）](configobject/UDG/20.15.2/S1TACID.md)

## 使用实例

假设运营商需要查看指定S1TAC号段与S1TAC组的绑定关系：S1TAC组为beijing，S1TAC号段为2：

```
LST S1TACID:TACGROUPNAME="beijing",TACSECNUM=2;
```

```

RETCODE = 0  操作成功。

结果如下
--------
  S1TAC段编号  =  2
指定S1TAC组名  =  beijing
  S1TAC起始ID  =  0x0001
  S1TAC截止ID  =  0x0010
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查看S1TAC与S1TAC组的绑定关系（LST-S1TACID）_97358679.md`
