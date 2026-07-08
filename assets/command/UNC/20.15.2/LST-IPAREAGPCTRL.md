---
id: UNC@20.15.2@MMLCommand@LST IPAREAGPCTRL
type: MMLCommand
name: LST IPAREAGPCTRL（查询基于位置分配IP地址策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPAREAGPCTRL
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于位置分配IP地址管理
- 基于位置分配IP地址策略管理
status: active
---

# LST IPAREAGPCTRL（查询基于位置分配IP地址策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询基于用户位置分配动态IP地址的策略。

## 注意事项

- 此命令执行后立即生效

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPAREAGPCTRL]] · 基于位置分配IP地址策略（IPAREAGPCTRL）

## 使用实例

显示基于位置分配的IP地址策略：

LST IPAREAGPCTRL:;

```
%%LST IPAREAGPCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
                 用户下线开关  = 关闭
           用户下线速度(个/秒) = 200
是否区分本网本地和本网异地用户 = 不区分
           GU漫游用户限制方式  = 去激活
        GU本网异地用户限制方式 = 去激活
          GU用户接入限制原因值 = 15
         LTE用户接入限制原因值 = 15
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPAREAGPCTRL.md`
