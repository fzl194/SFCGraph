# 显示通过OPS运行的应用程序的信息（DSP OPSPROCESSSTATE）

- [命令功能](#ZH-CN_CONCEPT_0000001600441189__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600441189__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600441189__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600441189__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600441189__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600441189__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600441189)

该命令用于显示通过OPS运行的应用程序的信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600441189)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600441189)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600441189)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| METHOD | 方式 | 可选必选说明：必选参数<br>参数含义：方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- current：当前信息。<br>- history：历史信息。<br>- verbose：详细信息。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600441189)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600441189)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 应用标识 | 应用标识。 |
| 命令 | 命令。 |
| 状态 | 状态。<br>- 初始状态: 进程初始状态。<br>- 运行状态: 进程运行状态。<br>- 输入: 输入状态。<br>- 停止: 停止状态。<br>- 退出: 退出状态。 |
| 进程ID | 进程ID。 |
