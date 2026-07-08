---
id: UDG@20.15.2@MMLCommand@ULD EXPFILE
type: MMLCommand
name: ULD EXPFILE（上传导出文件）
nf: UDG
version: 20.15.2
verb: ULD
object_keyword: EXPFILE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置管理
- 配置导出管理
status: active
---

# ULD EXPFILE（上传导出文件）

## 功能

本命令可以将FileServer上的导出文件上传到指定的SFTP服务器。

> **说明**
> 无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| FILETYPE | 导出文件类型 | 可选必选说明：必选参数<br>参数含义：标识导出文件的类型，用于指示系统需要将哪种类型的导出文件上传到SFTP服务器。<br>取值范围：<br>EXP_MML(EXP_MML)<br>默认值：无。<br>配置原则：无。 |
| MEID | 网元ID | 可选必选说明：该参数在<br>**“导出文件类型”**<br>配置为<br>“EXP_MML(EXP_MML)”<br>时为条件可选参数。<br>参数含义：标识网元对象，用于指示系统需要将哪一个网元的配置导出文件上传到SFTP服务器。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：<br>- 当不填写该参数时，本命令会选择前缀为“EXPMML_ALLME_”的配置导出文件上传。<br>- 当填写该参数时，本命令会先选择前缀为“EXPMML_ME<MEID>_”的配置导出文件上传，如“EXPMML_ME0_”。如果这样前缀的文件不存在，则会选择前缀为“EXPMML_ALLME_”的配置导出文件上传。<br>- 如果未找到符合匹配规则的文件，则命令执行报错，上传导出文件失败。<br>- 网元ID可以通过**LST ME**命令查询。 |
| IPTYPE | SFTP服务器IP地址类型 | 可选必选说明：必选参数。<br>参数含义：用于标识SFTP服务器的IP地址类型。<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无。<br>配置原则：无。 |
| IPV4 | SFTP服务器IP地址 | 可选必选说明：该参数在<br>**“SFTP服务器IP地址类型”**<br>配置为<br>“IPV4(IPV4)”<br>时为条件必选参数。<br>参数含义：用于标识SFTP服务器的IP地址。<br>取值范围：IPv4地址。<br>默认值：无。<br>配置原则：无。 |
| IPV6 | SFTP服务器IP地址 | 可选必选说明：该参数在<br>**“SFTP服务器IP地址类型”**<br>配置为<br>“IPV6(IPV6)”<br>时为条件必选参数。<br>参数含义：用于标识SFTP服务器的IP地址。<br>取值范围：IPv6地址。<br>默认值：无。<br>配置原则：无。 |
| FTPUSER | SFTP用户名 | 可选必选说明：必选参数。<br>参数含义：用于标识登录SFTP服务器的用户名。<br>取值范围：长度不超过128的字符串。<br>默认值：无。<br>配置原则：不支持逗号（,）、分号（;），等号（=）、双引号（"）、单引号（'），两个及以上的百分号（%），两个及以上的空格（ ）、mml报文起始符标识（+++）、mml报文结束符（--- END）。 |
| FTPPSSWD | SFTP密码 | 可选必选说明：必选参数。<br>参数含义：用于标识登录SFTP服务器的密码。<br>取值范围：长度不超过128的密码。<br>默认值：无。<br>配置原则：密码字符支持范围为大写字母（A~Z），小写字母（a~z），数字（0~9）和特殊字符（包括空格!"#$%&'()*+,-./\:;<=>?@[]^{_\|}~），填写范围之外的字符可能会导致导出文件上传到SFTP服务器失败。 |
| DSTF | 目标目录 | 可选必选说明：必选参数。<br>参数含义：用于标识SFTP传输的目标路径。<br>取值范围：长度不超过256的字符串。<br>默认值：无。<br>配置原则：由数字（0~9）、字母（a~z,A~Z）及特殊符号（~!@#*()^_-+{}[]\:./?%单空格）组成，且不能包含父目录符号（../）。 |
| FTPPORT | SFTP端口号 | 可选必选说明：可选参数。<br>参数含义：用于标识SFTP服务器的端口号。<br>取值范围：1～65535。<br>默认值：22。<br>配置原则：需要和真实的SFTP服务器端口一致，不填写则使用默认端口22。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXPFILE]] · 上传导出文件（EXPFILE）

## 使用实例

将网元ID为“0”的配置导出文件上传到指定的SFTP服务器：

ULD EXPFILE: FILETYPE=EXP_MML, MEID=0, IPTYPE=IPV4, IPV4="192.168.1.1", FTPUSER="root", FTPPSSWD=" ******* ", DSTF="/";

```
%%ULD EXPFILE: FILETYPE=EXP_MML, MEID=0, IPTYPE=IPV4, IPV4="192.168.1.1", FTPUSER="root", FTPPSSWD="
*****
", DSTF="/";%%
RETCODE = 0  操作成功

进度报文
--------
上报类型  =  ULD EXPFILE
    状态  =  进行中
  会话号  =  501
(结果个数 = 1)

---    END

%%ULD EXPFILE: FILETYPE=EXP_MML, MEID=0, IPTYPE=IPV4, IPV4="192.168.1.1", FTPUSER="root", FTPPSSWD="
*****
", DSTF="/";%%
RETCODE = 0  操作成功

进度报文
--------
上报类型  =  ULD EXPFILE
    状态  =  完成
  会话号  =  501
(结果个数 = 1)

共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/上传导出文件（ULD-EXPFILE）_89738541.md`
