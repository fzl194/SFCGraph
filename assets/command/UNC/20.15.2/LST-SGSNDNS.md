---
id: UNC@20.15.2@MMLCommand@LST SGSNDNS
type: MMLCommand
name: LST SGSNDNS（查询SGSN DNS域名策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSNDNS
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
- GnGp-SGSN_S10_S16_S3接口管理
- SGSN DNS解析
status: active
---

# LST SGSNDNS（查询SGSN DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询SGSN DNS域名策略配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS域名类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALL（ALL）”<br>- “RAI（RAI）”<br>- “NRI（NRI）”<br>- “RNC_ID（RNC ID）”<br>- “LAI（LAI）”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“RAI（RAI）”<br>或<br>“LAI（LAI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值 ：无 |
| RAC | 路由区域码 | 可选必选说明：可选参数<br>参数含义：该参数用来指定路由区域码<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“RAI（RAI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |
| NRI | NRI | 可选必选说明：可选参数<br>参数含义：该参数用来指定NRI（Net Resource Identify）。NRI用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“NRI（NRI）”<br>后生效。<br>数据来源：整网规划<br>取值范围： 0～1023<br>默认值： 无 |
| RNCID | RNC ID | 可选必选说明：可选参数<br>参数含义：该参数用来指定RNC标识。RNC标识用于在一个PLMN中唯一标识一个RNC。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“RNC_ID（RNC ID）”<br>后生效。<br>数据来源：整网规划<br>取值范围： 0～4096<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGSNDNS]] · SGSN DNS域名策略（SGSNDNS）

## 使用实例

查询所有SGSNDNS配置：

**LST SGSNDNS:;**

```
%%LST SGSNDNS:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
       域名类型  =  RAI
     位置区域码  =  0x01
 位置区域码范围  =  0x03
     路由区域码  =  0x05
 路由区域码范围  =  0x08
            NRI  =  NULL
        NRI范围  =  NULL
    NRI域名格式  =  标准方式
         RNC ID  =  NULL
     RNC ID范围  =  NULL
PLMN ID选择方式  =  标准方式
   移动国家代码  =  NULL
       移动网号  =  NULL
    DNS域名策略  =  .gprs
DNS域名组装形式  =  4位十进制MNC和MCC
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGSNDNS.md`
