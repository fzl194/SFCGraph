---
id: UNC@20.15.2@MMLCommand@LST NSSFFCSWITCH
type: MMLCommand
name: LST NSSFFCSWITCH（查询NSSF流控开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFFCSWITCH
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF流控管理
status: active
---

# LST NSSFFCSWITCH（查询NSSF流控开关）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF流控开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSSFFCSWITCH | NSSF流控开关 | 可选必选说明：可选参数<br>参数含义：该参数表示NSSF流控开关状态。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSSFFCSWITCH]] · NSSF流控开关（NSSFFCSWITCH）

## 使用实例

当运营商希望查询NSSF是否开启流控功能时，可以通过此命令查询NSSF的流控开关状态：

```
LST NSSFFCSWITCH:;
%%LST NSSFFCSWITCH:;%%
RETCODE = 0  执行成功

结果如下
-------------------------
    NSSF流控开关  =  打开
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSSFFCSWITCH.md`
