---
id: UNC@20.15.2@MMLCommand@LST ZCCONVERT
type: MMLCommand
name: LST ZCCONVERT（查询区域码转换策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ZCCONVERT
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
- 移动性管理
- 区域漫游限制管理
- 区域码转换
status: active
---

# LST ZCCONVERT（查询区域码转换策略）

## 功能

**适用网元：SGSN、MME**

此命令用于查询区域码转换策略。

## 注意事项

- 此命令执行后立即生效

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询区域码转换策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无<br>说明：对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO运营商标识。 对于本网用户，该参数是为该用户归属的MNO运营商标识。 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>配置为<br>“FOREIGN_USER（外网用户）”<br>或<br>“HOME_USER（本网用户）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：如果不输入该参数，系统会查询所有的“SUBRANGE（用户范围）”配置为“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”记录。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定区域码转换的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：只有<br>“SUBRANGE（用户范围）”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：如果不输入该参数，系统会查询所有“SUBRANGE（用户范围）”配置为“IMSI_PREFIX（指定IMSI前缀）”的配置记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ZCCONVERT]] · 区域码转换策略（ZCCONVERT）

## 使用实例

场景参见 [**ADD ZCCONVERT**](增加区域码转换策略(ADD ZCCONVERT)_26305378.md) 的命令使用实例。

- 查询本网用户区域码转换策略：
  LST ZCCONVERT: SUBRANGE=HOME_USER;
  ```
  %%LST ZCCONVERT: SUBRANGE=HOME_USER;%%
  RETCODE = 0  操作成功。

  输出结果如下
  -------------------------
            用户范围  =  本网用户
          运营商标识  =  45
            IMSI前缀  =  NULL
            转换策略  =  采用指定ZC
              区域码  =  0x1234
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询区域码转换策略(LST-ZCCONVERT)_72225249.md`
