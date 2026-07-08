---
id: UNC@20.15.2@MMLCommand@LST DEVICEINFO
type: MMLCommand
name: LST DEVICEINFO（查询设备档案信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DEVICEINFO
command_category: 查询类
applicable_nf:
- NWDAF
- SMF
- SPF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- 状态查询
status: active
---

# LST DEVICEINFO（查询设备档案信息）

## 功能

**适用NF：NWDAF、SMF、SPF**

该命令用于显示设备档案信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEVICEINFO]] · 设备档案信息（DEVICEINFO）

## 使用实例

查询设备档案信息

```
%% LST DEVICEINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
       网元类型  =  XXX
       	EOS时间  =  2027-12-31
   网元激活时间  =  2024-02-26
       网元版本  =  25.0.0
   网元补丁版本  =  25.0.0.1
       网元名称  =  XXX
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询设备档案信息（LST-DEVICEINFO）_54415745.md`
