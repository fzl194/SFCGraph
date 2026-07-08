---
id: UNC@20.15.2@MMLCommand@DSP NTPSFTD
type: MMLCommand
name: DSP NTPSFTD（查询NTP软参）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NTPSFTD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- NTP软参管理
status: active
---

# DSP NTPSFTD（查询NTP软参）

## 功能

该命令为专家维护命令，用于查询NTP软参值。

该命令仅适用于开局阶段调测或者维护的操作场景，当需要查询NTP软参配置信息时，操作员可以使用该命令实现这一目的。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NM | NTP功能模块 | 可选必选说明：必选参数。<br>参数含义：用于指定需要开启软参功能的模块号。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |
| CTRL | 控制字 | 可选必选说明：必选参数。<br>参数含义：用于指定本次操作设置的软参控制字。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NTPSFTD]] · NTP软参（NTPSFTD）

## 使用实例

1. 查询后台配置的时间同步策略。
  ```
  %%DSP NTPSFTD: NM=4, CTRL=1;%% 
  RETCODE = 0  操作成功
  操作结果如下
  ------------
  手工同步策略  =  priority_get_time_from_fst
  自动同步策略  =  auto_get_time_from_fst
  (结果个数 = 1)

  ---    END
  ```
2. 查询各节点生效的时间同步策略。
  ```
  %%DSP NTPSFTD: NM=4, CTRL=2;%%
  RETCODE = 0  操作成功
  操作结果如下
  ------------
  节点名称      手工同步策略                自动同步策略
  10.0.0.1      priority_get_time_from_fst  auto_get_time_from_fst
  10.0.0.2      priority_get_time_from_fst  auto_get_time_from_fst
  10.0.0.3      priority_get_time_from_fst  auto_get_time_from_fst
  10.0.0.4      priority_get_time_from_fst  auto_get_time_from_fst
  10.0.0.5      priority_get_time_from_fst  auto_get_time_from_fst
  (结果个数 = 5)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NTPSFTD.md`
