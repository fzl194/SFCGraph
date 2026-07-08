---
id: UNC@20.15.2@MMLCommand@LST RESTOFUNC
type: MMLCommand
name: LST RESTOFUNC（查询容灾功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESTOFUNC
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME容灾管理
- 容灾功能管理
status: active
---

# LST RESTOFUNC（查询容灾功能）

## 功能

**适用网元：MME**

本命令用于查询设备容灾功能的运行方式，以及业务恢复流程的方式。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [容灾功能（RESTOFUNC）](configobject/UNC/20.15.2/RESTOFUNC.md)

## 使用实例

查询设备容灾功能的运行方式，以及业务恢复流程的方式：

LST RESTOFUNC:;

```
%%LST RESTOFUNC:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
            业务恢复模式  =  一次呼叫恢复
        容灾功能运行模式  =  调测模式
             HSS注册策略  =  立即更新位置
恢复用户的合法性校验范围  =  1
                号段匹配  =  是
恢复用户的合法性校验范围  =  0
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾功能(LST-RESTOFUNC)_26146114.md`
