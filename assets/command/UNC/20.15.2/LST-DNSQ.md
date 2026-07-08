---
id: UNC@20.15.2@MMLCommand@LST DNSQ
type: MMLCommand
name: LST DNSQ（查询DNS查询控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNSQ
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS查询管理
status: active
---

# LST DNSQ（查询DNS查询控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询DNS查询控制的相关参数，包括DNS查询方式，DNS服务器组ID。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于表示签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “All（所有用户）”<br>- “SPECIFY（指定用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于系统根据该参数对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：当<br>“用户范围”<br>为<br>“SPECIFY（指定用户）”<br>时，此参数为必选参数。<br>数据来源：整网规划<br>取值范围：5~15数字<br>默认值：无<br>说明：没有配置IMSI前缀的记录，在IMSI前缀项上显示的结果为“EEEEEEEEEEEEEEE”。 |
| DNSUF | 域名后缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示域名后缀。<br>取值范围：0~255个字符<br>默认值：无<br>说明：- 按照域名后缀选择合适的DNS服务器。域名后缀在比较时从后向前进行最大匹配。<br>- 域名后缀支持配置为*。任何域名和*比较，都认为匹配。<br>- 域名后缀不能以“.”开始，也不能以“.”结束。<br>- 相同域名后缀下的IMSI前缀不能相同，相同IMSI前缀下的域名后缀不能相同。<br>- 该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）、通配符（*）和点（.）组成。<br>- 按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSQ]] · DNS查询控制参数（DNSQ）

## 使用实例

查询DNS查询控制的参数，命令格式如下：

LST DNSQ: SUBRANGE=All, DNSUF="gprs";

```
%%LST DNSQ: SUBRANGE=All, DNSUF="gprs";%% 
RETCODE = 0  操作成功。  

操作结果如下 
--------------           
     用户范围  =  所有用户          
     IMSI前缀  =  EEEEEEEEEEEEEEE           
     域名后缀  =  gprs              
   DNS解析方式 =  本地数据优先
   DNS查询方式 =  NAPTR      
DNS服务器组ID  =  1 
         描述  =  NULL
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNSQ.md`
