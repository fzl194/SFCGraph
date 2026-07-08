---
id: UNC@20.15.2@MMLCommand@LST IPSECPOLICYTM
type: MMLCommand
name: LST IPSECPOLICYTM（查询IPsec策略模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPSECPOLICYTM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec策略模板
status: active
---

# LST IPSECPOLICYTM（查询IPsec策略模板）

## 功能

该命令用于查询IPsec策略模板。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略模板名称 | 可选必选说明：可选参数<br>参数含义：策略模板名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SEQUENCENUMBER | 策略模板序列号 | 可选必选说明：可选参数<br>参数含义：策略模板序列号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是1~10000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPsec策略模板（IPSECPOLICYTM）](configobject/UNC/20.15.2/IPSECPOLICYTM.md)

## 使用实例

查询IPsec策略模板：

```
LST IPSECPOLICYTM:POLICYNAME="temp3",SEQUENCENUMBER=1;

RETCODE = 0  操作成功

结果如下
-------------------------
        策略模板名称  =  temp3
              序列号  =  1
       IKE对等体名称  =  peer1
   IPsec安全提议名称  =  prop1
             ACL名称  =  acl1
             ACL编号  =  3000
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
        自动切回开关  =  未使能
          扩展序列号  =  未使能
      数据流可信使能  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPsec策略模板（LST-IPSECPOLICYTM）_96204446.md`
