---
id: UNC@20.15.2@MMLCommand@LST CHGPLMNCG
type: MMLCommand
name: LST CHGPLMNCG（查询PLMN-CG配置参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGPLMNCG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN CG 配置
status: active
---

# LST CHGPLMNCG（查询PLMN-CG配置参数）

## 功能

**适用网元：SGSN**

该命令用于查询为PLMN配置的CG IP地址。该PLMN上产生的话单会优先发往这些已配置过的CG。

## 注意事项

- 如果有输入参数，则显示与输入参数均匹配的CG IP配置记录；如果没有输入参数，则显示所有CG IP配置记录。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PLMN的移动国家号码。<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [PLMN-CG配置参数（CHGPLMNCG）](configobject/UNC/20.15.2/CHGPLMNCG.md)

## 使用实例

1. 查询PLMN配置的优先发送话单的CG IP地址：
  LST CHGPLMNCG:;

  ```
  %%LST CHGPLMNCG:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  移动国家码    移动网号     IP地址类型   CG1的IPV4地址     CG2的IPV4地址        CG3的IPV4地址        CG4的IPV4地址        CG5的IPV4地址    
  123           002          IPV4         172.23.44.66      255.255.255.255      255.255.255.255      255.255.255.255      255.255.255.255
  123           01           IPV4         172.23.0.1        172.23.0.2           172.23.0.3           172.23.0.4           172.23.0.5     
  仍有后续报告输出
  ---    END

  %%LST CHGPLMNCG:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------------------
  移动国家码     移动网号     IP地址类型     CG1的IPV6地址                  CG2的IPV6地址                  CG3的IPV6地址                  CG4的IPV6地址                CG5的IPV6地址
  123            031          IPV6           2001:db8:10:19:44:55:10:12     2001:db8:10:19:44:55:10:87     2001:db8:10:19:44:55:10:68     2001:db8:10:19:44:55:10:72   2001:db8:10:19:44:55:10:94                 
  123            031          IPV6           2001:db8:10:19:44:55:10:22     2001:db8:10:19:44:55:10:23     2001:db8:10:19:44:55:10:24     2001:db8:10:19:44:55:10:25     2001:db8:10:19:44:55:10:26               
  (结果个数 = 4)
  共有2个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PLMN-CG配置参数(LST-CHGPLMNCG)_26145388.md`
