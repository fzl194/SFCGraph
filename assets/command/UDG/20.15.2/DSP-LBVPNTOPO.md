---
id: UDG@20.15.2@MMLCommand@DSP LBVPNTOPO
type: MMLCommand
name: DSP LBVPNTOPO（查询CSLB VPN对应的MPE或SFE拓扑）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBVPNTOPO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- VPN管理
- VPN拓扑信息
status: active
---

# DSP LBVPNTOPO（查询CSLB VPN对应的MPE或SFE拓扑）

## 功能

查询CSLB服务侧VPN对应的转发拓扑。转发拓扑由高字节TB、低字节TB以及TP信息表示，分为VPN对应的VNRS转发拓扑与VPN对应的CSLB转发拓扑

## 注意事项

- 该命令仅限于开发和测试使用。
- 该命令批量下发可能导致执行超时。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：VPN名称<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0~63<br>配置原则：公网填“_public_”<br>默认值：无 |
| TOPOTYPE | 拓扑类型 | 可选必选说明：必选参数<br>参数含义：改参数用于指定是查询VNRS的拓扑还是查询CSLB的拓扑<br>数据来源：本端规划<br>取值范围：<br>- “MPE(CSLB的转发面拓扑)”<br>- “SFE(VNRS的转发面拓扑)”<br>默认值：无 |
| HTB | 高字节TB | 可选必选说明：可选参数<br>参数含义：表示TB的高16位。TB全称是Target Blade，即目标板<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295<br>默认值：无 |
| LTB | 低字节TB | 可选必选说明：可选参数<br>参数含义：表示TB的低32位。TB全称是Target Blade，即目标板<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295<br>默认值：无 |
| TP | TP | 可选必选说明：可选参数<br>参数含义：表示目标端口。TP全称是Target Port<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295<br>默认值：无 |

## 操作的配置对象

- [CSLB VPN对应的MPE或SFE拓扑（LBVPNTOPO）](configobject/UDG/20.15.2/LBVPNTOPO.md)

## 使用实例

- 查询CSLB服务侧VPN对应的转发地址信息
  DSP LBVPNTOPO: VPNNAME="_public_", TOPOTYPE=SFE, LTB=70;

  ```
  RETCODE = 0  操作成功

  操作结果如下:
  -------------
     VPN名称  =  _public_
    拓扑类型  =  VNRS Topo
    高字节TB  =  0
    低字节TB  =  70
         TP   =  4098
  	 状态  =  Normal
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSLB-VPN对应的MPE或SFE拓扑(DSP-LBVPNTOPO)_29627076.md`
