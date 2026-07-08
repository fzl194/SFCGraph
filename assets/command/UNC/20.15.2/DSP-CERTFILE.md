---
id: UNC@20.15.2@MMLCommand@DSP CERTFILE
type: MMLCommand
name: DSP CERTFILE（查询证书）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CERTFILE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# DSP CERTFILE（查询证书）

## 功能

本命令用于查询 OM Portal 内在 “ 安全 > 证书管理 > 证书与证书集管理 ” 页面内显示的所有证书。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CERTNAME | 证书名称 | 可选必选说明：可选参数。<br>参数含义：证书文件名称，支持模糊查询。<br>取值范围：字符串类型，输入长度范围为0~192。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CERTFILE]] · 证书（CERTFILE）

## 使用实例

查询系统证书。

```
%%DSP CERTFILE: CERTNAME="testCA";%%
RETCODE = 0  操作成功

      证书名称  =  testCA
      证书类型  =  CA
      创建时间  =  2021/07/02 22:24:41
   证书CN Name  =  Huawei
        序列号  =  32e54c68906184e94619cde4d7923353c79dafe8
        颁发者  =  O=Huawei, C=CN
        持有者  =  O=Huawei, C=CN
      生效时间  =  2021/06/28 09:39:38
      失效时间  =  2021/09/25 09:39:38
      到期天数  =  82
吊销列表分发点  =  NULL
          状态  =  即将过期
      关联状态  =  未关联
      所属应用  =  NULL
      场景名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询证书（DSP-CERTFILE）_70642071.md`
