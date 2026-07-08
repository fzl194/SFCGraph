---
id: UDG@20.15.2@MMLCommand@DSP LOGSERVERSTC
type: MMLCommand
name: DSP LOGSERVERSTC（查询日志中心5分钟内消息统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LOGSERVERSTC
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

# DSP LOGSERVERSTC（查询日志中心5分钟内消息统计信息）

## 功能

该命令用于查询日志中心5分钟内的日志统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOGSERVERSTC]] · 日志中心5分钟内消息统计信息（LOGSERVERSTC）

## 使用实例

查询日志中心5分钟内的统计信息，可通过如下命令查询：

```
DSP LOGSERVERSTC:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
日志ID       模块名称       日志类型    日志数量 

134615040    SSPBASE        诊断日志    4         
135335941    DEBUG          诊断日志    21        
135335976    DEBUG          诊断日志    1  
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LOGSERVERSTC.md`
