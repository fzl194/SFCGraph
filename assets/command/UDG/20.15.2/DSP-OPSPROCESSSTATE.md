---
id: UDG@20.15.2@MMLCommand@DSP OPSPROCESSSTATE
type: MMLCommand
name: DSP OPSPROCESSSTATE（显示通过OPS运行的应用程序的信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OPSPROCESSSTATE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 开放可编程系统
status: active
---

# DSP OPSPROCESSSTATE（显示通过OPS运行的应用程序的信息）

## 功能

该命令用于显示通过OPS运行的应用程序的信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| METHOD | 方式 | 可选必选说明：必选参数<br>参数含义：方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- current：当前信息。<br>- history：历史信息。<br>- verbose：详细信息。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OPSPROCESSSTATE]] · 通过OPS运行的应用程序的信息（OPSPROCESSSTATE）

## 使用实例

- 显示通过OPS运行的应用程序的信息：
  ```
  DSP OPSPROCESSSTATE:METHOD=current;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  应用标识  =  608
    进程ID  =  8451
      状态  =  初始状态
      命令  =  _ops_frame_execute.pyc _get_all_env.py
  (结果个数 = 1)
  ---    END
  ```
- 显示通过OPS运行的应用程序的历史信息：
  ```
  DSP OPSPROCESSSTATE:METHOD=history;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
          命令  =  _ops_frame_conditon.pyc _get_all_env.py
      应用标识  =  1
      所属类型  =  助手
      所属名称  =  _get_all_env.py
    背景标志位  =  TRUE
  触发运行时间  =  Aug 14 2018 10:23:26
  运行启动时间  =  Aug 14 2018 10:23:27
  运行结束时间  =  Aug 14 2018 10:23:27
          结果  =  正常
  (结果个数 = 1)
  ---    END
  ```
- 显示通过OPS运行的应用程序的详细信息：
  ```
  DSP OPSPROCESSSTATE:METHOD=verbose;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
          命令  =  _ops_frame_conditon.pyc autoscaling_autoconfig.py
      应用标识  =  2
        进程ID  =  4354
      所属类型  =  助手
      所属名称  =  autoscaling_autoconfig.py
    背景标志位  =  TRUE
  触发运行时间  =  Dec 20 2017 18:24:39
  运行启动时间  =  Dec 20 2017 18:24:40
          状态  =  运行状态
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示通过OPS运行的应用程序的信息（DSP-OPSPROCESSSTATE）_00441189.md`
