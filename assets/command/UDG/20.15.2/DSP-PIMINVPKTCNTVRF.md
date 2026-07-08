---
id: UDG@20.15.2@MMLCommand@DSP PIMINVPKTCNTVRF
type: MMLCommand
name: DSP PIMINVPKTCNTVRF（查询PIM实例无效报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PIMINVPKTCNTVRF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP组播
- PIM配置
- PIM实例的非法报文计数
status: active
---

# DSP PIMINVPKTCNTVRF（查询PIM实例无效报文统计）

## 功能

该命令用于显示PIM实例无效报文统计。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PIMINVPKTCNTVRF]] · PIM实例无效报文统计（PIMINVPKTCNTVRF）

## 使用实例

显示PIM实例无效报文统计：

```
DSP PIMINVPKTCNTVRF:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast;
```

```
RETCODE = 0 操作成功

结果如下
-------------------------
查询返回结果
                               VPN实例名称 = _public_
                                    地址族 = IPv4单播
                  无效PIM版本的PIM报文计数 = 0
                 无效报文类型的PIM报文计数 = 0
               无效的报文长度的PIM报文计数 = 0
                 无效的校验和的PIM报文计数 = 0
          无效组播源地址的Register报文计数 = 0
          无效组播组地址的Register报文计数 = 0
            目的地址非法的Register报文计数 = 0
     无效组播源地址的Register-Stop报文计数 = 0
     无效组播组地址的Register-Stop报文计数 = 0
       目的地址非法的Register-Stop报文计数 = 0
       源地址不是RP的Register-Stop报文计数 = 0
                 目的地址非法的CRP报文计数 = 0
                  无效CRP地址的CRP报文计数 = 0
               无效的报文长度的CRP报文计数 = 0
            无效的CRP Adv长度的CRP报文计数 = 0
               无效组播组地址的CRP报文计数 = 0
              目的地址非法的Assert报文计数 = 0
            报文源地址非法的Assert报文计数 = 0
            无效组播源地址的Assert报文计数 = 0
            无效组播组地址的Assert报文计数 = 0
            无效的报文长度的Assert报文计数 = 0
                无效的Payload的BSR报文计数 = 0
               无效的报文长度的BSR报文计数 = 0
              无效的Scope掩码的BSR报文计数 = 0
               无效组播组地址的BSR报文计数 = 0
        不是CBSR却收到BSR消息的BSR报文计数 = 0
                  无效BSR地址的BSR报文计数 = 0
               无效的哈希长度的BSR报文计数 = 0
               无效报文源地址的BSR报文计数 = 0
           无效地址列表的PIM Hello报文计数 = 0
         无效的报文长度的PIM Hello报文计数 = 0
     无效的Holdtime长度的PIM Hello报文计数 = 0
无效的LanPruneDelay长度的PIM Hello报文计数 = 0
  无效的DR Priority长度的PIM Hello报文计数 = 0
 无效的GenerationID长度的PIM Hello报文计数 = 0
           无效目的地址的PIM Hello报文计数 = 0
         无效报文源地址的PIM Hello报文计数 = 0
        无效组播源地址的Join/Prune报文计数 = 0
        无效组播组地址的Join/Prune报文计数 = 0
        无效的上游邻居的Join/Prune报文计数 = 0
        无效报文源地址的Join/Prune报文计数 = 0
          无效目的地址的Join/Prune报文计数 = 0
        无效的报文长度的Join/Prune报文计数 = 0
无效目的地址的Auto-RP Announcement报文计数 = 0
  无效源地址的Auto-RP Announcement报文计数 = 0
    无效下一跳Auto-RP Announcement报文计数 = 0
    无效源接口Auto-RP Announcement报文计数 = 0
   无效错误长度的Auto-RP Discovery报文计数 = 0
     无效RP地址的Auto-RP Discovery报文计数 = 0
       无效源地址Auto-RP Discovery报文计数 = 0
       无效组播组Auto-RP Discovery报文计数 = 0
         无效TTL Auto-RP Discovery报文计数 = 0
       无效源接口Auto-RP Discovery报文计数 = 0
(结果个数 = 1)
----- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PIM实例无效报文统计（DSP-PIMINVPKTCNTVRF）_49961038.md`
