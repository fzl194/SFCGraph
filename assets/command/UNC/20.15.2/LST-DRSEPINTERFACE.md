---
id: UNC@20.15.2@MMLCommand@LST DRSEPINTERFACE
type: MMLCommand
name: LST DRSEPINTERFACE（查询快速隔离接口）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRSEPINTERFACE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRSEPINTERFACE（查询快速隔离接口）

## 功能

该命令用于在免交换组网下组成热备容灾关系的网元间DCI通道变化时，查询已添加的逻辑接口。

## 注意事项

该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于配置容灾组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于配置接口名称。可通过<br>[**LST DRSEPINTERFACE**](查询快速隔离接口（LST DRSEPINTERFACE）_86255389.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRSEPINTERFACE]] · 故障隔离接口（DRSEPINTERFACE）

## 使用实例

查询添加的故障隔离接口。

```
%%LST DRSEPINTERFACE: DRGROUPID=1, IFNAME="itf1";%%
RETCODE = 0  操作成功

结果如下
--------
容灾组标识  =  1
    接口名  =  itf1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DRSEPINTERFACE.md`
