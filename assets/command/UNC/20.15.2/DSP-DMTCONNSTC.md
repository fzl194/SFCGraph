---
id: UNC@20.15.2@MMLCommand@DSP DMTCONNSTC
type: MMLCommand
name: DSP DMTCONNSTC（查询Diameter链路及消息收发统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DMTCONNSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 连接信息
status: active
---

# DSP DMTCONNSTC（查询Diameter链路及消息收发统计信息）

## 功能

该命令用于查询Diameter链路及消息收发统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMTCONNSTC]] · Diameter链路及消息收发统计信息（DMTCONNSTC）

## 使用实例

查询Diameter链路及消息收发统计信息：

```
DSP DMTCONNSTC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
            协议类型  =  TCP协议
              端类型  =  服务端
        本端IPv4地址  =  192.168.1.1
        对端IPv4地址  =  192.168.1.3
      连接所在组件ID  =  0x1db0002
        连接组项索引  =  1
从生产者接收消息统计  =  0
  发送生产者消息统计  =  0
  发送消费者消息统计  =  0
从消费者接收消息统计  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DMTCONNSTC.md`
