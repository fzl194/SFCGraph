---
id: UDG@20.15.2@MMLCommand@LST PODHEALCPUTHR
type: MMLCommand
name: LST PODHEALCPUTHR（查询对应PODTYPE的配置记录）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PODHEALCPUTHR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST PODHEALCPUTHR（查询对应PODTYPE的配置记录）

## 功能

当前版本此命令可正常下发，但配置不生效。

该命令用于查询对应PODTYPE的配置记录。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | POD类型 | 可选必选说明：可选参数<br>参数含义：用于设置POD类型。可通过<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODHEALCPUTHR]] · 对应PODTYPE下的阈值配置（PODHEALCPUTHR）

## 使用实例

查询对应PODTYPE的配置记录

```
%%LST PODHEALCPUTHR:;%%
RETCODE = 0  操作成功

结果如下
--------
POD 类型         空载阈值（%）  过载阈值（%）  

vsm-pod          10             70                         
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询对应PODTYPE的配置记录（LST-PODHEALCPUTHR）_24833370.md`
