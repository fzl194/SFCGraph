---
id: UNC@20.15.2@MMLCommand@OPR SETPRTGRPSPEC
type: MMLCommand
name: OPR SETPRTGRPSPEC（操作设置保护组规格值）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: SETPRTGRPSPEC
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 保护组管理
status: active
---

# OPR SETPRTGRPSPEC（操作设置保护组规格值）

## 功能

该命令用于设置保护组规格值。

外部网关路由器只与保护组内ISU/APU之间建立BFD会话，备路由也只到保护组内ISU/APU的ECMP路由。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SPECVALUE | 保护组规格值 | 可选必选说明：必选参数<br>参数含义：该参数用于表达保护组规格值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SETPRTGRPSPEC]] · 操作设置保护组规格值（SETPRTGRPSPEC）

## 使用实例

假如运营商只想让外部网关路由器与最多4个ISU/APU建立BFD会话，设置保护组规格值为4。

```
%%OPR SETPRTGRPSPEC: SPECVALUE=4;%%
RETCODE = 0  操作成功

结果如下
--------
结果说明  =  set protection group spec success
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-SETPRTGRPSPEC.md`
