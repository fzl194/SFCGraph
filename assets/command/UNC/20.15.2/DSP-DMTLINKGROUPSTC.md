---
id: UNC@20.15.2@MMLCommand@DSP DMTLINKGROUPSTC
type: MMLCommand
name: DSP DMTLINKGROUPSTC（显示Diameter链路组信息和链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DMTLINKGROUPSTC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- Diameter链路组信息
status: active
---

# DSP DMTLINKGROUPSTC（显示Diameter链路组信息和链路信息）

## 功能

该命令用来查询Diameter链路组信息和链路信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [Diameter链路组信息和链路信息（DMTLINKGROUPSTC）](configobject/UNC/20.15.2/DMTLINKGROUPSTC.md)

## 使用实例

查询Diameter链路组信息和链路信息：

```
DSP DMTLINKGROUPSTC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
            本端表项索引  =  0
            对端表项索引  =  1
                选路模式  =  激活模式
              本端主机名  =  01010101.huawei.com
              对端主机名  =  01010103.huawei.com
    从生产者接收消息统计  =  69
      发送生产者消息统计  =  35
      发送消费者消息统计  =  69
    从消费者接收消息统计  =  35
                协议类型  =  TCP协议
端类型（Client Or Server）=  服务端
   IP类型（IPv4 Or IPv6） =  IPv4
              本端IP地址  =  192.168.1.1
              对端IP地址  =  192.168.1.3
          连接所在组件ID  =  0x1db0006
            连接组项索引  =  1
（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Diameter链路组信息和链路信息（DSP-DMTLINKGROUPSTC）_00600337.md`
