---
id: UNC@20.15.2@MMLCommand@LST ADDRTACGROUP
type: MMLCommand
name: LST ADDRTACGROUP（查询TAC组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRTACGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配位置区管理
- 地址分配TAC组
status: active
---

# LST ADDRTACGROUP（查询TAC组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来查询指定TAC组或者所有TAC组的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGROUPNAME | TAC组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADDRTACGROUP]] · TAC组（ADDRTACGROUP）

## 使用实例

查询所有TAC组的信息：

```
%%LST ADDRTACGROUP:;%%
RETCODE = 0 操作成功

结果如下
-------
TAC组名称  =  1
  TAC类型  =  S1TAC
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ADDRTACGROUP.md`
