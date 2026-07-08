---
id: UDG@20.15.2@MMLCommand@LST IPSECPOLICY
type: MMLCommand
name: LST IPSECPOLICY（查询IPsec策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSECPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec策略
status: active
---

# LST IPSECPOLICY（查询IPsec策略）

## 功能

该命令用于查询IPsec策略。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 序列号 | 可选必选说明：可选参数<br>参数含义：序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSECPOLICY]] · IPsec策略（IPSECPOLICY）

## 使用实例

查询IPsec策略：

```
LST IPSECPOLICY:POLICYNAME="pol2",SEQUENCENUMBER=1;

RETCODE = 0  操作成功

结果如下
-------------------------
            策略名称  =  pol2
              序列号  =  1
            策略模式  =  ISAKMP模式
            模板模式  =  无
             ACL编号  =  0
             ACL名称  =  NULL
  去使能SA按流量计长  =  FALSE
SA按流量计长 (kbyte)  =  1843200
      SA按时计长 (s)  =  3600
                 PFS  =  无
    选择DSCP入方向值  =  输入DSCP编码
    输入DSCP入方向值  =  1
    选择DSCP出方向值  =  输入DSCP编码
    输入DSCP出方向值  =  1
              抗重放  =  未配置
      抗重放窗口大小  =  无
        清除分片标记  =  否
      加密前分片报文  =  否
入方向限速 (kbyte/s)  =  0
出方向限速 (kbyte/s)  =  0
            日志使能  =  否
          策略组标识  =  1
            工作模式  =  轮询
        自动切回开关  =  未使能
          扩展序列号  =  未使能
      数据流可信使能  =  否
            模板名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPsec策略（LST-IPSECPOLICY）_80751066.md`
