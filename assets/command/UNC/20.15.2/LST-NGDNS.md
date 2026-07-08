---
id: UNC@20.15.2@MMLCommand@LST NGDNS
type: MMLCommand
name: LST NGDNS（查询DNS运行参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGDNS
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# LST NGDNS（查询DNS运行参数）

## 功能

**适用NF：AMF、SMF**

该命令用于查询DNS域名解析流程相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMESWITCH | 优选融合MME开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否打开优选融合MME开关。当打开优选融合MME开关后，如果解析到的IP地址为融合MME，该IP地址会被优先选择。<br>数据来源：全网规划<br>取值范围：<br>- MME_ON（打开）<br>- MME_OFF（关闭）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGDNS]] · DNS运行参数（NGDNS）

## 使用实例

查询DNS运行参数：

```
LST NGDNS:;
%%LST NGDNS:;%%
RETCODE = 0  操作成功

结果如下
--------------
                   优选融合MME开关  =  打开
         N26接口本网IP地址选择策略  =  仅使用IPv6地址
                      总共发送次数  =  3
                响应超时时长(毫秒)  =  1000
一级Cache等待二级Cache响应时长(秒)  =  3
                        服务器组ID  =  11
                       DNS解析方式  =  本地数据优先
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNS运行参数（LST-NGDNS）_09652584.md`
