---
id: UDG@20.15.2@MMLCommand@LST LACID
type: MMLCommand
name: LST LACID（查看LAC与LAC组的绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LACID
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
- LAC段
status: active
---

# LST LACID（查看LAC与LAC组的绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看指定LAC号段与LAC组的绑定关系或者配置的所有LAC号段和LAC组的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | 指定LAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LACSECNUM | Lac 段编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～23999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LACID]] · 从LAC组内删除一个LAC（LACID）

## 使用实例

假设运营商需要查看指定LAC号段与LAC组的绑定关系：LAC组为beijing，LAC号段为2：

```
LST LACID: LACGROUPNAME="beijing", LACSECNUM=2;
```

```

RETCODE = 0  操作成功。

结果如下
--------
  LAC段编号  =  2
指定LAC组名  =  beijing
  LAC起始ID  =  0x0001
  LAC截止ID  =  0x0010
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查看LAC与LAC组的绑定关系（LST-LACID）_82837199.md`
