---
id: UNC@20.15.2@MMLCommand@LST RCLICIGNSW
type: MMLCommand
name: LST RCLICIGNSW（查询注册中心用户数license忽略开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RCLICIGNSW
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- License管理
status: active
---

# LST RCLICIGNSW（查询注册中心用户数license忽略开关）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF/VLR到注册中心进行用户注册时是否忽略注册中心用户数License控制结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/RCLICIGNSW]] · 注册中心用户数license忽略开关（RCLICIGNSW）

## 使用实例

运营商希望查询SMSF/VLR到注册中心进行用户注册时是否忽略注册中心用户数License控制结果，执行如下命令：

```
LST RCLICIGNSW:;
%%LST RCLICIGNSW:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
注册中心用户数 license忽略开关 =  打开

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询注册中心用户数license忽略开关（LST-RCLICIGNSW）_54815038.md`
