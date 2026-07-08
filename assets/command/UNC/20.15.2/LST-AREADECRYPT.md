---
id: UNC@20.15.2@MMLCommand@LST AREADECRYPT
type: MMLCommand
name: LST AREADECRYPT（查询基于LAC/RAC关闭加密配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AREADECRYPT
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- 基于LAC_RAC关闭加密配置
status: active
---

# LST AREADECRYPT（查询基于LAC/RAC关闭加密配置）

## 功能

**适用网元：SGSN**

该命令用于查询基于路由区/位置区关闭加密的配置记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDTYPE | 标识类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定区域的标识类型。<br>数据来源：整网规划<br>取值范围：<br>“LA(位置区)”<br>，<br>“RA(路由区)”<br>。<br>配置原则：<br>- LA：表示该区域标识类型为位置区。<br>- RA：表示该区域标识类型为路由区。<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值： 无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值： 无 |
| LAC | 位置区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码<br>前提条件：该参数在<br>“标识类型”<br>设置为<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREADECRYPT]] · 基于LAC/RAC关闭加密配置（AREADECRYPT）

## 使用实例

查询标识类型为“RA(路由区)”的所有记录：

LST AREADECRYPT: IDTYPE=RA;

```
%%LST AREADECRYPT: IDTYPE=RA;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 标识类型  移动国家代码  移动网号  位置区域码  路由区域码

 路由区    456           02        0x1234      0x12      
 路由区    888           12        0x0FFF      0xFF      
 路由区    888           12        0xA12F      0x23      
 路由区    888           12        0xA12F      0x24      
 路由区    888           12        0xABCD      0x12      
 路由区    888           12        0xABCD      0x13      
 路由区    888           12        0xFFF0      0x23      
 路由区    888           12        0xFFFF      0xFF      
 路由区    999           13        0x1234      0x00      
(结果个数 = 9)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于LAC_RAC关闭加密配置(LST-AREADECRYPT)_26305452.md`
