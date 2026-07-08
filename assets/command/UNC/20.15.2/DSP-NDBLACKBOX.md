---
id: UNC@20.15.2@MMLCommand@DSP NDBLACKBOX
type: MMLCommand
name: DSP NDBLACKBOX（查询ND黑匣子信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NDBLACKBOX
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- ND
status: active
---

# DSP NDBLACKBOX（查询ND黑匣子信息）

## 功能

该命令用于查询ND的黑匣子记录的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | IPv6 ND黑匣子类型 | 可选必选说明：必选参数<br>参数含义：该参数指定IPv6 ND黑匣子类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- COMP：黑匣子组件信息。<br>- HA：黑匣子HA状态信息。<br>- PIPE：黑匣子组件管道信息。<br>- PACKET：黑匣子组件包信息。<br>- ASSERT：黑匣子组件异常信息。<br>- MSG：黑匣子组件消息记录信息。<br>默认值：无 |
| PID | ND PID | 可选必选说明：必选参数<br>参数含义：该参数用来指定ND组件PID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [ND黑匣子信息（NDBLACKBOX）](configobject/UNC/20.15.2/NDBLACKBOX.md)

## 使用实例

- 查询ND组件的黑匣子记录的信息：
  ```
  DSP NDBLACKBOX: TYPE=COMP, PID="0x73003A";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果信息

          CompPid CompState     Cause  Date  Hour   Min   Sec
       2155347983         0         0    20     8    44    42

       2155347984         0         0    20     8    44    42

       2155347985         1         0    20     8    44    42

       2154102904         0         0    20     8    44    42

          7995409         0         0    20     8    44    42

          2359352         0         0    20     8    44    42

         10879009         0         0    20     8    44    42

          6946838         0         0    20     8    44    42

          2293768         0         0    20     8    44    42

          6946834         1         0    20     8    44    42

          6946834         0         0    20     8    44    42

       2155347985         0         0    20     8    44    43

  (结果个数 = 12)
  ---    END
  ```
- 查询黑匣子记录的管道信息：
  ```
  DSP NDBLACKBOX: TYPE=PIPE, PID="0x73003A";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果信息

          CompPid      PipeId   PipeMsg ServiceID  Date  Hour   Min   Sec
          2359352     1572872         3       888    20     8    44    42

       2155347985  3221749802         1         8    20     8    45     2

  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询ND黑匣子信息（DSP-NDBLACKBOX）_00840973.md`
