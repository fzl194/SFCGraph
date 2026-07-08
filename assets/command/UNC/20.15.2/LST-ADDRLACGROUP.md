---
id: UNC@20.15.2@MMLCommand@LST ADDRLACGROUP
type: MMLCommand
name: LST ADDRLACGROUP（查询LAC组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRLACGROUP
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
- 地址分配LAC组
status: active
---

# LST ADDRLACGROUP（查询LAC组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来查询指定LAC组或者所有LAC组的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADDRLACGROUP]] · LAC组（ADDRLACGROUP）

## 使用实例

查询指定LAC组“beijing”的LAC组配置信息：

```
%%LST ADDRLACGROUP: ;%%
RETCODE = 0  操作成功

结果如下
--------
LAC组名  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ADDRLACGROUP.md`
