---
id: UNC@20.15.2@MMLCommand@STP S1BALANCE
type: MMLCommand
name: STP S1BALANCE（停止S1接口均衡操作）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: S1BALANCE
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口均衡管理
status: active
---

# STP S1BALANCE（停止S1接口均衡操作）

## 功能

**适用网元：MME**

此命令用于停止正在进行的系统自动均衡迁移任务。

## 注意事项

- 此命令执行后立即生效。
- 此命令执行后，迁移任务完全停止需要大约12秒的时间。
- 使用此命令停止迁移后，未开始启动迁移的eNodeB将不在迁移，已经启动迁移的eNodeB将继续完成迁移流程，迁移任务执行结果可以通过DSP S1BALANCE命令查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1BALANCE]] · S1接口均衡操作（S1BALANCE）

## 使用实例

1. 停止S1接口均衡操作：STP S1BALANCE:;
  ```

  %%STP S1BALANCE:;%% 
  RETCODE = 0  操作成功。 
 
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-S1BALANCE.md`
