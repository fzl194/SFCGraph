---
id: UDG@20.15.2@MMLCommand@DSP ELECTSERVICE
type: MMLCommand
name: DSP ELECTSERVICE（查询仲裁服务状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ELECTSERVICE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 仲裁服务状态
status: active
---

# DSP ELECTSERVICE（查询仲裁服务状态）

## 功能

该命令用于查询仲裁服务状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [仲裁服务状态（ELECTSERVICE）](configobject/UDG/20.15.2/ELECTSERVICE.md)

## 使用实例

查询仲裁服务开关状态：

```
DSP ELECTSERVICE:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
       仲裁服务开关状态 =  使能
(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询仲裁服务状态（DSP-ELECTSERVICE）_59103974.md`
