---
id: UNC@20.15.2@MMLCommand@LST SRVNODERATPRI
type: MMLCommand
name: LST SRVNODERATPRI（查询获取RAT Type的优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVNODERATPRI
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- 获取RAT方式的优先级
status: active
---

# LST SRVNODERATPRI（查询获取RAT Type的优先级）

## 功能

**适用NF：GGSN**

该命令用来查询整机RAT类型的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数表示当前配置的网元类型。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODERATPRI]] · 获取RAT Type的优先级（SRVNODERATPRI）

## 使用实例

查询整机RAT类型的优先级：

```
%%LST SRVNODERATPRI:;%%
RETCODE = 0  操作成功

结果如下
--------
           网元类型  =  GGSN
RAT类型的第一优先级  =  RAT
RAT类型的第二优先级  =  SGSNIP
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SRVNODERATPRI.md`
