---
id: UDG@20.15.2@MMLCommand@LST LOGDIC
type: MMLCommand
name: LST LOGDIC（查询日志模型信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LOGDIC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 日志管理
status: active
---

# LST LOGDIC（查询日志模型信息）

## 功能

该命令用于查询日志字典，日志字典中包含定义日志模型的基本信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LOGDIC]] · 日志模型信息（LOGDIC）

## 使用实例

全量查询日志字典（模型）信息，可通过如下命令查询：

```
LST LOGDIC:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
日志ID       日志名称                            模块ID      特性名称         级别    Trap标志    是否记录日志标志    是否记录安全日志标志 
134615040    DOPRA_LOG                           2054        SSPBASE          4       NO          YES                 NO                    
134807558    HAF_SWITCH_SUCCESS                  2057        SYSTEM           2       YES         YES                 NO                    
134807559    HAF_SWITCH_FAIL                     2057        SYSTEM           2       YES         YES                 NO                                    

(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-LOGDIC.md`
