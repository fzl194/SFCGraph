---
id: UNC@20.15.2@MMLCommand@LST SCPPARA
type: MMLCommand
name: LST SCPPARA（查询SCP参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCPPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- SCP信息管理
status: active
---

# LST SCPPARA（查询SCP参数）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询SCP参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCPPARA]] · SCP参数（SCPPARA）

## 使用实例

查询SCP参数。

```
%%LST SCPPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
服务发现策略  =  LOCAL_FIRST
    SCPDOMAIN  =  domain1
SCPDOMAIN开关  =  ON
发现周期 (分钟)  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCP参数（LST-SCPPARA）_52469392.md`
