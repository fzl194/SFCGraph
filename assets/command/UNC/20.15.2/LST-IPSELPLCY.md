---
id: UNC@20.15.2@MMLCommand@LST IPSELPLCY
type: MMLCommand
name: LST IPSELPLCY（查询IP地址选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPSELPLCY
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
- IP地址选择策略
status: active
---

# LST IPSELPLCY（查询IP地址选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于查询S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口IP地址选择策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLRANGE | 控制范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定命令生效的范围。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(缺省策略)”<br>- “SPECIFY(指定IMSI)”<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户的IMSI。<br>前提条件：该参数在<br>“CTRLRANGE(控制范围)”<br>设置为<br>“SPECIFY(指定IMSI)”<br>有效。<br>数据来源：整网规划<br>取值范围：0~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSELPLCY]] · IP地址选择策略（IPSELPLCY）

## 使用实例

场景参见 [**ADD IPSELPLCY**](增加IP地址选择策略(ADD IPSELPLCY)_72225141.md) 的命令使用实例。

- 查询S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口的IP地址选择策略：
  LST IPSELPLCY:;
  ```
  %%LST IPSELPLCY:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
  控制范围        IMSI              LTE接口本网IP地址选择策略    LTE接口漫游IP地址选择策略    GU接口本网IP地址选择策略    GU接口漫游IP地址选择策略   描述      	

  缺省策略        NULL              仅使用IPv4地址               仅使用IPv4地址               仅使用IPv4地址              仅使用IPv4地址             DeviceTest		
  指定IMSI        123031501000001   仅使用IPv6地址               仅使用IPv4地址               仅使用IPv6地址              仅使用IPv4地址             MobileTest
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IP地址选择策略(LST-IPSELPLCY)_26145462.md`
