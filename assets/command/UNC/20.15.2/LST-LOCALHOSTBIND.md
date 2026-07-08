---
id: UNC@20.15.2@MMLCommand@LST LOCALHOSTBIND
type: MMLCommand
name: LST LOCALHOSTBIND（查询Diameter本端主机与Diameter本端主机组的关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALHOSTBIND
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diamter本端主机组绑定
status: active
---

# LST LOCALHOSTBIND（查询Diameter本端主机与Diameter本端主机组的关联关系）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询Diameter本端主机与Diameter本端主机组的绑定信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGRPNAME | Diameter本端信息组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter本端主机组名。要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALHOSTBIND]] · Diameter本端主机与Diameter本端主机组的关联关系（LOCALHOSTBIND）

## 使用实例

查询Diameter本端主机与Diameter本端主机组的关联关系，被查询的Diameter本端主机组名为“abc”：

```
LST LOCALHOSTBIND: LOCGRPNAME="abc";
```

```

RETCODE = 0 操作成功。

Diameter本端主机组内的Diameter主机信息
--------------------------------------
Diameter本端信息组名  =  abc
  Diameter本端主机名  =  aaa
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCALHOSTBIND.md`
