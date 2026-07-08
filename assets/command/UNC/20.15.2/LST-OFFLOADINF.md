---
id: UNC@20.15.2@MMLCommand@LST OFFLOADINF
type: MMLCommand
name: LST OFFLOADINF（查询迁移配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OFFLOADINF
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 迁移控制
status: active
---

# LST OFFLOADINF（查询迁移配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询迁移配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFFLOADINF]] · 迁移配置信息（OFFLOADINF）

## 使用实例

查询迁移配置信息：

LST OFFLOADINF:;

```
%%LST OFFLOADINF:;%%
RETCODE = 0  操作成功。

迁移配置信息
------------
      迁移模式周期路由更新定时器(s)  =  60
              第一阶段迁移时间(min)  =  1
                         非广播 RAI  =  111111111111
                         POOL区标识  =  0
                         NULL NRI值  =  9
                           迁移速率  =  高速
 迁移时是否设置Force To Standby信元  =  是
迁移时是否设置Follow On Proceed信元  =  是
          根据UE无线能力选择USN开关  =  关闭
          根据UE无线能力选择UNC开关  =  关闭
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询迁移配置信息（LST-OFFLOADINF）_26146096.md`
