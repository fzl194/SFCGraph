---
id: UDG@20.15.2@MMLCommand@LST RUFAULTTOLERANCE
type: MMLCommand
name: LST RUFAULTTOLERANCE（查询资源单元故障容忍时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RUFAULTTOLERANCE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# LST RUFAULTTOLERANCE（查询资源单元故障容忍时间）

## 功能

该命令用于查询资源单元故障容忍时间。

需要设置资源单元故障容忍时间前，可以通过该命令显示当前的资源单元故障时间配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RUFAULTTOLERANCE]] · 资源单元故障容忍时间（RUFAULTTOLERANCE）

## 使用实例

查询资源单元故障容忍时间配置：

```
LST RUFAULTTOLERANCE:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
     RU故障容忍时间（s）  =  NULL
 RU故障反向容忍时间（s）  =  NULL
    RU故障容忍时间（ms）  =  9000
RU故障反向容忍时间（ms）  =  8000
软仲裁选主容忍时间（ms）  =  4000
软仲裁停主容忍时间（ms）  =  4000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RUFAULTTOLERANCE.md`
