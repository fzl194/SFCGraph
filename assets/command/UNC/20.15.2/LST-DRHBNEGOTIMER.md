---
id: UNC@20.15.2@MMLCommand@LST DRHBNEGOTIMER
type: MMLCommand
name: LST DRHBNEGOTIMER（查询容灾定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRHBNEGOTIMER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRHBNEGOTIMER（查询容灾定时器）

## 功能

该命令用于查询容灾定时器。

## 注意事项

- 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：可选参数<br>参数含义：该参数用来标识一个容灾组，该标识必须存在于容灾组信息中，容灾组信息可以使用<br>[**LST DRGROUPINFO**](查询容灾组信息（LST DRGROUPINFO）_74835153.md)<br>命令查询。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [容灾定时器（DRHBNEGOTIMER）](configobject/UNC/20.15.2/DRHBNEGOTIMER.md)

## 使用实例

- 查询所有的容灾定时器:
  ```
  %%LST DRHBNEGOTIMER:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                   容灾组标识 = 1
    心跳消息重传时间(100毫秒) = 10
    协商消息重传时间(100毫秒) = 20
                     重传次数 = 3
  OM通道心跳探测时长(100毫秒) = 10
           OM通道心跳重传次数 = 3
  (结果个数 = 1)

  ---    END
  ```
- 查询指定容灾组的容灾定时器:
  ```
  %%LST DRHBNEGOTIMER: DRGROUPID=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                   容灾组标识 = 1
    心跳消息重传时间(100毫秒) = 10
    协商消息重传时间(100毫秒) = 20
                     重传次数 = 3
  OM通道心跳探测时长(100毫秒) = 10
           OM通道心跳重传次数 = 3
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询容灾定时器（LST-DRHBNEGOTIMER）_23235162.md`
