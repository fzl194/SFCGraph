---
id: UNC@20.15.2@MMLCommand@LST SMARTCFG
type: MMLCommand
name: LST SMARTCFG（查询智能用户功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMARTCFG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- Smartphone控制基础功能
status: active
---

# LST SMARTCFG（查询智能用户功能）

## 功能

**适用网元：SGSN**

该命令用于查询SMART用户功能。包括SMART用户识别功能、识别SMART用户的SERVICE REQUEST门限、SMART用户是否禁止启用DT功能和SMART用户是否禁止启用去活非活动PDP功能。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMARTCFG]] · 智能用户功能（SMARTCFG）

## 使用实例

查询智能用户功能：

LST SMARTCFG:;

```
%%LST SMARTCFG:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                  是否启用SMART用户识别功能  =  是
识别SMART用户的SERVICE REQUEST门限(times/h)  =  60
                SMART用户是否禁止启用DT功能  =  否
     SMART用户是否禁止启用去活非活动PDP功能  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询智能用户功能（LST-SMARTCFG）_72225429.md`
