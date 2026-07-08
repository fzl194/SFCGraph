---
id: UNC@20.15.2@MMLCommand@LST INNERSTAT
type: MMLCommand
name: LST INNERSTAT（查询内统配置参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INNERSTAT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 内统管理
status: active
---

# LST INNERSTAT（查询内统配置参数）

## 功能

**适用NF：AMF**

该命令用于查询内统配置参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATPRIORITY | 内统优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内统优先级。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULTPRIORITY（默认优先级）<br>- LOWPRORITY（低优先级）<br>- HIGHPRORITY（高优先级）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/INNERSTAT]] · 内统配置参数（INNERSTAT）

## 使用实例

查询内统配置参数，执行如下命令：

```
%%LST INNERSTAT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
内统优先级  内统的日志打印周期  内统的日志打印周期失效时间  

默认优先级  5分钟               0
低优先级    5分钟      	        0
高优先级    5分钟               0
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-INNERSTAT.md`
