---
id: UDG@20.15.2@MMLCommand@DSP SDRPLYSUBINFO
type: MMLCommand
name: DSP SDRPLYSUBINFO（显示所有策略订阅者信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRPLYSUBINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRPLYSUBINFO（显示所有策略订阅者信息）

## 功能

该命令用于显示所有策略订阅者信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERID | 订阅者ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示订阅者ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [所有策略订阅者信息（SDRPLYSUBINFO）](configobject/UDG/20.15.2/SDRPLYSUBINFO.md)

## 使用实例

查询所有策略订阅者信息：

```
%%DSP SDRPLYSUBINFO: SUBSCRIBERID="TopicRelationCacher";%%
RETCODE = 0  操作成功

结果如下
--------
            订阅者ID = TopicRelationCacher
                策略 = AppRoute
未收到同步响应的数量 = 0
  收到同步响应的数量 = 0
      同步核查的次数 = 0
    未同步核查的次数 = 0
             Nonce值 = 86
            阻塞数量 = 0
  策略发送成功的数量 = 86
              会话ID = 1
            超时总数 = 0
  存储策略的内存状态 = 300-86-128
          是否在流控 = FALSE
    流控状态切换次数 = 0
            流控次数 = 0
    观察者是否是最新 = FALSE
最新的观察者请求时间 = 2022-06-02 15:29:38.086190192
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示所有策略订阅者信息（DSP-SDRPLYSUBINFO）_71652974.md`
